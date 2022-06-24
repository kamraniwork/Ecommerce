# security

1. [throttling](#use-throttling)
    
* ###### use throttling:
    user can not more than 3 each per second
    and use to Viewsets class in views.py file:
    ```python
  from pytimeparse.timeparse import timeparse
  from rest_framework.throttling import UserRateThrottle
    
  class CustomThrottlingUser(UserRateThrottle):
      scope = 'apps'
      rate = '3/1s'
    
      def parse_rate(self, rate):
    
          if rate is None:
              return None, None
          num, period = rate.split('/')
          num_requests = int(num)
          duration = timeparse(period)
          return num_requests, duration
    
  def get_throttles(self):
      throttle_classes = (CustomThrottlingUser,)
      return [throttle() for throttle in throttle_classes]
    ```
