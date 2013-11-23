from direct.directtools.DirectGeometry import LineNodePath
from panda3d.core import *
from panda3d.ode import *
from direct.showbase.ShowBase import ShowBase
import sys

class Application(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.lines = LineNodePath(parent = render, thickness = 3.0, colorVec = Vec4(1, 0, 0, 1))

        # Load the self.smiley and self.frowney models
        self.smiley = loader.loadModel("smiley.egg")
        self.smiley.reparentTo(render)
        self.smiley.setPos(-5, 0, -5)
        self.frowney = loader.loadModel("frowney.egg")
        self.frowney.reparentTo(render)
        self.frowney.setPos(-12.5, 0, -7.5)
         
        # Setup our physics self.world
        self.world = OdeWorld()
        self.world.setGravity(0, 0, -9.81)
         
        # Setup the body for the self.smiley
        self.smileyBody = OdeBody(self.world)
        M = OdeMass()
        M.setSphere(5000, 1.0)
        self.smileyBody.setMass(M)
        self.smileyBody.setPosition(self.smiley.getPos(render))
        self.smileyBody.setQuaternion(self.smiley.getQuat(render))
         
        # Now, the body for the self.frowney
        self.frowneyBody = OdeBody(self.world)
        M = OdeMass()
        M.setSphere(5000, 1.0)
        self.frowneyBody.setMass(M)
        self.frowneyBody.setPosition(self.frowney.getPos(render))
        self.frowneyBody.setQuaternion(self.frowney.getQuat(render))
         
        # Create the joints
        smileyJoint = OdeBallJoint(self.world)
        smileyJoint.attach(self.smileyBody, None) # Attach it to the environment
        smileyJoint.setAnchor(0, 0, 0)
        frowneyJoint = OdeBallJoint(self.world)
        frowneyJoint.attach(self.smileyBody, self.frowneyBody)
        frowneyJoint.setAnchor(-5, 0, -5)
         
        # Set the camera position
        base.disableMouse()
        base.camera.setPos(0, 50, -7.5)
        base.camera.lookAt(0, 0, -7.5)

        self.accept("escape", sys.exit)

        taskMgr.doMethodLater(0.5, self.simulationTask, "Physics Simulation")

    def drawLines(self):
        # Draws lines between the self.smiley and self.frowney.
        self.lines.reset()
        self.lines.drawLines([((self.frowney.getX(), self.frowney.getY(), self.frowney.getZ()),
                        (self.smiley.getX(), self.smiley.getY(), self.smiley.getZ())),
                       ((self.smiley.getX(), self.smiley.getY(), self.smiley.getZ()),
                        (0, 0, 0))])
        self.lines.create()

    # The task for our simulation
    def simulationTask(self, task):
        # Step the simulation and set the new positions
        # self.drawLines()
        self.world.quickStep(globalClock.getDt())
        self.frowney.setPosQuat(render, self.frowneyBody.getPosition(), Quat(self.frowneyBody.getQuaternion()))
        self.smiley.setPosQuat(render, self.smileyBody.getPosition(), Quat(self.smileyBody.getQuaternion()))
        self.drawLines()
        return task.cont

app = Application()
app.drawLines()
app.run()