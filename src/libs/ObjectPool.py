
class PoolReusable:
  def __init__(self, size=5):
    self._max = max;
    self.size = 1;
    self._reusables = [Reusable() for _ in range(size)]

  def acquire(self):
    if len(self._reusables) == 0:
     raise Exception("Pool empty")
    return self._reusables.pop()

  def release(self, reusable):
    self._reusables.append(reusable)

  def use(self):
    reusable = self.acquire();
    return self.release(reusable);

  def available(self):
    return len(self._reusables);


class Reusable:
    pass