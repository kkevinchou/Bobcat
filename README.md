Bobcat
======
/usr/share/panda3d/direct/task/Task.py
Traceback (most recent call last):
  File "/usr/lib/python2.7/threading.py", line 551, in __bootstrap_inner
    self.run()
  File "/usr/lib/python2.7/threading.py", line 504, in run
    self.__target(*self.__args, **self.__kwargs)
  File "/home/kevin/workspace/Bobcat/server/lib/game.py", line 43, in main
    self.update(fixed_update_dt)
  File "/home/kevin/workspace/Bobcat/server/game/game.py", line 31, in update
    self.a.taskMgr.step()
  File "/usr/share/panda3d/direct/task/Task.py", line 456, in step
    signal.signal(signal.SIGINT, self.keyboardInterruptHandler)
ValueError: signal only works in main thread