import time

class PoolReusable:
  def __init__(self, size=5):
    self._max = max;
    self.size = 1;
    self._reusables = [Reusable(_) for _ in range(size)]

  def acquire(self):
    if len(self._reusables) == 0:
     raise Exception("Pool empty")
    return self._reusables.pop()

  def release(self, reusable):
    self._reusables.append(reusable)
    return self.available();

  def use(self):
    reusable = self.acquire();
    print("Available after internal acquire " + str(self.available()))
    available = self.release(reusable);
    print("Available after internal release " + str(self.available()))
    return available

  def available(self):
    return len(self._reusables);


class Reusable:
  def __init__(self, id):
    print("Created " + str(id))
  pass