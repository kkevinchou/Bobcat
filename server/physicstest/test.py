from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from panda3d.physics import *
import sys
from direct.showbase.DirectObject import DirectObject


class Application(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.cam.setPos(0, -50, 10)
        self.setupCD()
        self.setupPhysics()
        self.addSmiley()
        self.addFloor()

        self.accept("escape", sys.exit)
        self.accept("arrow_left", self.setKey, ["left", 1])
        self.accept("arrow_right", self.setKey, ["right", 1])
        self.accept("arrow_up", self.setKey, ["forward", 1])
        self.accept("arrow_left-up", self.setKey, ["left", 0])
        self.accept("arrow_right-up", self.setKey, ["right", 0])
        self.accept("arrow_up-up", self.setKey, ["forward", 0])

        self.keyMap = {}
        self.keyMap['left'] = 0
        self.keyMap['right'] = 0
        self.keyMap['forward'] = 0

        taskMgr.add(self.move,"moveTask")

    def setKey(self, key, value):
        self.keyMap[key] = value

    def move(self, task):
        if (self.keyMap["left"]):
            pass
            # self.ralph.setH(self.ralph.getH() + 300 * globalClock.getDt())
        if (self.keyMap["right"]!=0):
            pass
            # self.ralph.setH(self.ralph.getH() - 300 * globalClock.getDt())
        if (self.keyMap["forward"]!=0):
            self.phys_object.set_velocity(Vec3(0, 10, 0))
            # self.ralph.setY(self.ralph, -25 * globalClock.getDt())

        return task.cont


    def thrust(self):
        thrustNode = ForceNode("thrust")
        self.phys.attachNewNode(thrustNode)
        self.thrustForce = LinearVectorForce(-100, 0, 0)
        self.thrustForce.setMassDependent(1)
        thrustNode.addForce(self.thrustForce)
        base.physicsMgr.addLinearForce(self.thrustForce)

    def setupCD(self):
        base.cTrav = CollisionTraverser()
        base.cTrav.showCollisions(render)
        self.notifier = CollisionHandlerEvent()
        self.notifier.addInPattern("%fn-in-%in")
        self.notifier.addOutPattern("%fn-out-%in")
        self.accept("smiley-in-floor", self.onCollisionStart)
        self.accept("smiley-out-floor", self.onCollisionEnd)

        self.pusher = PhysicsCollisionHandler()


    def setupPhysics(self):
        base.enableParticles()
        gravNode = ForceNode("gravity")
        render.attachNewNode(gravNode)
        gravityForce = LinearVectorForce(0, 0, -9.81)
        gravNode.addForce(gravityForce)
        base.physicsMgr.addLinearForce(gravityForce)

    def addSmiley(self):
        self.actor = ActorNode("physics")
        self.phys_object = self.actor.getPhysicsObject()
        self.phys_object.setMass(10)

        self.phys = render.attachNewNode(self.actor)
        base.physicsMgr.attachPhysicalNode(self.actor)

        self.smiley = loader.loadModel("smiley")
        self.smiley.reparentTo(self.phys)
        self.phys.setPos(0, 0, 10)

        col = self.smiley.attachNewNode(CollisionNode("smiley"))
        col.node().addSolid(CollisionSphere(0, 0, 0, 1.1))
        col.show()

        self.pusher.addCollider(col, self.phys)
        base.cTrav.addCollider(col, self.pusher)

    def addFloor(self):
        floor = render.attachNewNode(CollisionNode("floor"))
        floor.node().addSolid(CollisionPlane(Plane(Vec3(0, 0, 1),
        Point3(0, 0, 0))))
        floor.show()

    def onCollisionStart(self, entry):
        print 'Collision Start'
        # base.physicsMgr.addLinearForce(self.thrustForce)

    def onCollisionEnd(self, entry):
        print 'Collision End'
        # base.physicsMgr.removeLinearForce(self.thrustForce)

app = Application()
app.run()