from rest_framework.throttling import SimpleRateThrottle

class LoginBurstRateThrottle(SimpleRateThrottle):
    scope = "login_burst"
    rate = "5/min"  # opcional

    def get_cache_key(self, request, view):
        ip = request.META.get("REMOTE_ADDR")
        return f"login_burst_{ip}" if ip else None

    def wait(self):
        return super().wait()
