# from pandac.PandaModules import * 
# ConfigVariableManager.getGlobalPtr().listVariables()
# ConfigVariableString("window-type","none").setValue("none") 

from direct.directtools.DirectGeometry import LineNodePath

from panda3d.core import (
    Vec3,
    Vec4,
    CardMaker,
    Quat

)

from panda3d.ode import (
    OdeWorld,
    OdeSimpleSpace,
    OdeJointGroup,
    OdeBoxGeom,
    OdePlaneGeom,
    OdeBody,
    OdeMass,
    OdeSphereGeom

)

from direct.showbase.ShowBase import ShowBase
import sys

class Application(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.smiley = loader.loadModel("smiley")
        self.smiley.set_scale(1)
        # self.cam.set_pos(0, -50, 25)

        self.setup_ODE()
        self.add_ground()
        self.add_static_box(1, 1, 1)
        self.s1 = self.add_smiley(0, 0, 50)
        self.s2 = self.add_smiley(0, 0, 40)

        self.accept("escape", sys.exit)
        self.accept('a', self.velocity)
        taskMgr.add(self.update_ODE, "update_ODE")
        self.accept('on_collision', self.on_collision)

    def velocity(self):
        taskMgr.popupControls()
        self.s2.set_linear_vel(0, 0, 10)

    def setup_ODE(self):
        # Setup our physics self.world
        self.world = OdeWorld()
        self.world.setGravity(0, 0, -9.81)
        self.world.initSurfaceTable(1)
        self.world.setSurfaceEntry(0, 0, 200, 0.7, 0.2, 0.9, 0.00001, 0.0, 0.002)

        self.space = OdeSimpleSpace()
        self.space.setAutoCollideWorld(self.world)
        self.contacts = OdeJointGroup()
        self.space.setAutoCollideJointGroup(self.contacts)
        self.space.setCollisionEvent("on_collision")

    def on_collision(self, entry):
        geom1 = entry.getGeom1()
        geom2 = entry.getGeom2()
        body1 = entry.getBody1()
        body2 = entry.getBody2()

        print body1, body2

    def add_ground(self):
        cm = CardMaker("ground")
        cm.setFrame(-1, 1, -1, 1)
        ground = render.attachNewNode(cm.generate())
        ground.setColor(0.5, 0.7, 0.8)
        ground.lookAt(0, 0, -1)
        groundGeom = OdePlaneGeom(self.space, Vec4(0, 0, 1, 0))

    def add_smiley(self, x, y, z):
        sm = render.attachNewNode("smiley-instance")
        sm.setPos(x, y, z)
        self.smiley.instanceTo(sm)

        body = OdeBody(self.world)
        mass = OdeMass()
        mass.setSphereTotal(10, 1)
        body.setMass(mass)
        body.setPosition(sm.getPos())
        geom = OdeSphereGeom(self.space, 1)
        geom.setBody(body)

        sm.setPythonTag("body", body)

        return body

    def add_static_box(self, x, y, z):
        self.box = OdeBoxGeom(self.space, Vec3(x, y, z))
        self.box.set_position(0, 0, 25)

    def draw_box(self, box):
        line_collection = LineNodePath(parent=render, thickness=1.0, colorVec=Vec4(1, 0, 0, 1))
        pos = box.get_position()
        lengths = box.get_lengths()

        x = pos[0]
        y = pos[1]
        z = pos[2]

        half_width = lengths[0] / 2
        half_length = lengths[1] / 2
        half_height = lengths[2] / 2

        lines = [
            # Bottom Face
            ((x - half_width, y - half_length, z - half_height), (x + half_width, y - half_length, z - half_height)),
            ((x + half_width, y - half_length, z - half_height), (x + half_width, y + half_length, z - half_height)),
            ((x + half_width, y + half_length, z - half_height), (x - half_width, y + half_length, z - half_height)),
            ((x - half_width, y + half_length, z - half_height), (x - half_width, y - half_length, z - half_height)),
            # Top Face
            ((x - half_width, y - half_length, z + half_height), (x + half_width, y - half_length, z + half_height)),
            ((x + half_width, y - half_length, z + half_height), (x + half_width, y + half_length, z + half_height)),
            ((x + half_width, y + half_length, z + half_height), (x - half_width, y + half_length, z + half_height)),
            ((x - half_width, y + half_length, z + half_height), (x - half_width, y - half_length, z + half_height)),
            # Vertical Lines
            ((x - half_width, y - half_length, z - half_height), (x - half_width, y - half_length, z + half_height)),
            ((x + half_width, y - half_length, z - half_height), (x + half_width, y - half_length, z + half_height)),
            ((x + half_width, y + half_length, z - half_height), (x + half_width, y + half_length, z + half_height)),
            ((x - half_width, y + half_length, z - half_height), (x - half_width, y + half_length, z + half_height)),
        ]

        line_collection.drawLines(lines)
        line_collection.create()

    def update_ODE(self, task):
        self.space.autoCollide()
        self.world.quickStep(globalClock.getDt())

        self.draw_box(self.box)

        for smiley in render.findAllMatches("smiley-instance"):
            body = smiley.getPythonTag("body")
            smiley.setPosQuat(body.getPosition(), Quat(body.getQuaternion()))

        self.contacts.empty()
        return task.cont