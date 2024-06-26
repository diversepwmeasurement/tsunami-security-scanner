"""HTTP header field names."""

import enum


class HttpHeaderFields(enum.Enum):
  """HTTP header field definition from https://guava.dev/releases/snapshot/api/docs/com/google/common/net/HttpHeaders.html.

  Attributes:
    list: Get all header fields.
    get_from_lower: Get header field name from a case insensitive name.
  """

  # HTTP Request and Response header fields

  CACHE_CONTROL = "Cache-Control"
  CONTENT_LENGTH = "Content-Length"
  CONTENT_TYPE = "Content-Type"
  DATE = "Date"
  PRAGMA = "Pragma"
  VIA = "Via"
  WARNING = "Warning"

  # HTTP Request header fields

  ACCEPT = "Accept"
  ACCEPT_CHARSET = "Accept-Charset"
  ACCEPT_ENCODING = "Accept-Encoding"
  ACCEPT_LANGUAGE = "Accept-Language"
  ACCESS_CONTROL_REQUEST_HEADERS = "Access-Control-Request-Headers"
  ACCESS_CONTROL_REQUEST_METHOD = "Access-Control-Request-Method"
  AUTHORIZATION = "Authorization"
  CONNECTION = "Connection"
  COOKIE = "Cookie"
  CROSS_ORIGIN_RESOURCE_POLICY = "Cross-Origin-Resource-Policy"
  EARLY_DATA = "Early-Data"
  EXPECT = "Expect"
  FROM = "From"
  FORWARDED = "Forwarded"
  FOLLOW_ONLY_WHEN_PRERENDER_SHOWN = "Follow-Only-When-Prerender-Shown"
  HOST = "Host"
  HTTP2_SETTINGS = "HTTP2-Settings"
  IF_MATCH = "If-Match"
  IF_MODIFIED_SINCE = "If-Modified-Since"
  IF_NONE_MATCH = "If-None-Match"
  IF_RANGE = "If-Range"
  IF_UNMODIFIED_SINCE = "If-Unmodified-Since"
  LAST_EVENT_ID = "Last-Event-ID"
  MAX_FORWARDS = "Max-Forwards"
  ORIGIN = "Origin"
  ORIGIN_ISOLATION = "Origin-Isolation"
  PROXY_AUTHORIZATION = "Proxy-Authorization"
  RANGE = "Range"
  REFERER = "Referer"
  REFERRER_POLICY = "Referrer-Policy"
  NO_REFERRER = "no-referrer"
  NO_REFFERER_WHEN_DOWNGRADE = "no-referrer-when-downgrade"
  SAME_ORIGIN = "same-origin"
  STRICT_ORIGIN = "strict-origin"
  ORIGIN_WHEN_CROSS_ORIGIN = "origin-when-cross-origin"
  STRICT_ORIGIN_WHEN_CROSS_ORIGIN = "strict-origin-when-cross-origin"
  UNSAFE_URL = "unsafe-url"
  SERVICE_WORKER = "Service-Worker"
  TE = "TE"
  UPGRADE = "Upgrade"
  UPGRADE_INSECURE_REQUESTS = "Upgrade-Insecure-Requests"
  USER_AGENT = "User-Agent"

  # HTTP Response header fields

  ACCEPT_RANGES = "Accept-Ranges"
  ACCESS_CONTROL_ALLOW_HEADERS = "Access-Control-Allow-Headers"
  ACCESS_CONTROL_ALLOW_METHODS = "Access-Control-Allow-Methods"
  ACCESS_CONTROL_ALLOW_ORIGIN = "Access-Control-Allow-Origin"
  ACCESS_CONTROL_ALLOW_PRIVATE_NETWORK = "Access-Control-Allow-Private-Network"
  ACCESS_CONTROL_ALLOW_CREDENTIALS = "Access-Control-Allow-Credentials"
  ACCESS_CONTROL_EXPOSE_HEADERS = "Access-Control-Expose-Headers"
  ACCESS_CONTROL_MAX_AGE = "Access-Control-Max-Age"
  AGE = "Age"
  ALLOW = "Allow"
  CONTENT_DISPOSITION = "Content-Disposition"
  CONTENT_ENCODING = "Content-Encoding"
  CONTENT_LANGUAGE = "Content-Language"
  CONTENT_LOCATION = "Content-Location"
  CONTENT_MD5 = "Content-MD5"
  CONTENT_RANGE = "Content-Range"
  CONTENT_SECURITY_POLICY = "Content-Security-Policy"
  CONTENT_SECURITY_POLICY_REPORT_ONLY = "Content-Security-Policy-Report-Only"
  X_CONTENT_SECURITY_POLICY = "X-Content-Security-Policy"
  X_CONTENT_SECURITY_POLICY_REPORT_ONLY = "X-Content-Security-Policy-Report-Only"
  X_WEBKIT_CSP = "X-WebKit-CSP"
  X_WEBKIT_CSP_REPORT_ONLY = "X-WebKit-CSP-Report-Only"
  CROSS_ORIGIN_EMBEDDER_POLICY = "Cross-Origin-Embedder-Policy"
  CROSS_ORIGIN_EMBEDDER_POLICY_REPORT_ONLY = "Cross-Origin-Embedder-Policy-Report-Only"
  CROSS_ORIGIN_OPENER_POLICY = "Cross-Origin-Opener-Policy"
  ETAG = "ETag"
  EXPIRES = "Expires"
  LAST_MODIFIED = "Last-Modified"
  LINK = "Link"
  LOCATION = "Location"
  KEEP_ALIVE = "Keep-Alive"
  NO_VARY_SEARCH = "No-Vary-Search"
  ORIGIN_TRIAL = "Origin-Trial"
  P3P = "P3P"
  PROXY_AUTHENTICATE = "Proxy-Authenticate"
  REFRESH = "Refresh"
  REPORT_TO = "Report-To"
  RETRY_AFTER = "Retry-After"
  SERVER = "Server"
  SERVER_TIMING = "Server-Timing"
  SERVICE_WORKER_ALLOWED = "Service-Worker-Allowed"
  SET_COOKIE = "Set-Cookie"
  SET_COOKIE2 = "Set-Cookie2"
  SOURCE_MAP = "SourceMap"
  SUPPORTS_LOADING_MODE = "Supports-Loading-Mode"
  STRICT_TRANSPORT_SECURITY = "Strict-Transport-Security"
  TIMING_ALLOW_ORIGIN = "Timing-Allow-Origin"
  TRAILER = "Trailer"
  TRANSFER_ENCODING = "Transfer-Encoding"
  VARY = "Vary"
  WWW_AUTHENTICATE = "WWW-Authenticate"
  DNT = "DNT"
  X_CONTENT_TYPE_OPTIONS = "X-Content-Type-Options"
  X_DEVICE_IP = "X-Device-IP"
  X_DEVICE_REFERER = "X-Device-Referer"
  X_DEVICE_ACCEPT_LANGUAGE = "X-Device-Accept-Language"
  X_DEVICE_REQUESTED_WITH = "X-Device-Requested-With"
  X_DO_NOT_TRACK = "X-Do-Not-Track"
  X_FORWARDED_FOR = "X-Forwarded-For"
  X_FORWARDED_PROTO = "X-Forwarded-Proto"
  X_FORWARDED_HOST = "X-Forwarded-Host"
  X_FORWARDED_PORT = "X-Forwarded-Port"
  X_FRAME_OPTIONS = "X-Frame-Options"
  X_POWERED_BY = "X-Powered-By"
  PUBLIC_KEY_PINS = "Public-Key-Pins"
  PUBLIC_KEY_PINS_REPORT_ONLY = "Public-Key-Pins-Report-Only"
  X_REQUEST_ID = "X-Request-ID"
  X_REQUESTED_WITH = "X-Requested-With"
  X_USER_IP = "X-User-IP"
  X_DOWNLOAD_OPTIONS = "X-Download-Options"
  X_XSS_PROTECTION = "X-XSS-Protection"
  X_DNS_PREFETCH_CONTROL = "X-DNS-Prefetch-Control"
  PING_FROM = "Ping-From"
  PING_TO = "Ping-To"
  PURPOSE = "Purpose"
  X_PURPOSE = "X-Purpose"
  X_MOZ = "X-Moz"
  DEVICE_MEMORY = "Device-Memory"
  DOWNLINK = "Downlink"
  ECT = "ECT"
  RTT = "RTT"
  SAVE_DATA = "Save-Data"
  VIEWPORT_WIDTH = "Viewport-Width"
  WIDTH = "Width"
  PERMISSIONS_POLICY = "Permissions-Policy"
  SEC_CH_PREFERS_COLOR_SCHEME = "Sec-CH-Prefers-Color-Scheme"
  ACCEPT_CH = "Accept-CH"
  CRITICAL_CH = "Critical-CH"
  SEC_CH_UA = "Sec-CH-UA"
  SEC_CH_UA_ARCH = "Sec-CH-UA-Arch"
  SEC_CH_UA_MODEL = "Sec-CH-UA-Model"
  SEC_CH_UA_PLATFORM = "Sec-CH-UA-Platform"
  SEC_CH_UA_PLATFORM_VERSION = "Sec-CH-UA-Platform-Version"
  SEC_CH_UA_FULL_VERSION_LIST = "Sec-CH-UA-Full-Version-List"
  SEC_CH_UA_MOBILE = "Sec-CH-UA-Mobile"
  SEC_CH_UA_WOW64 = "Sec-CH-UA-WoW64"
  SEC_CH_UA_BITNESS = "Sec-CH-UA-Bitness"
  SEC_CH_VIEWPORT_WIDTH = "Sec-CH-Viewport-Width"
  SEC_CH_VIEWPORT_HEIGHT = "Sec-CH-Viewport-Height"
  SEC_CH_DPR = "Sec-CH-DPR"
  SEC_FETCH_DEST = "Sec-Fetch-Dest"
  SEC_FETCH_MODE = "Sec-Fetch-Mode"
  SEC_FETCH_SITE = "Sec-Fetch-Site"
  SEC_FETCH_USER = "Sec-Fetch-User"
  SEC_METADATA = "Sec-Metadata"
  SEC_TOKEN_BINDING = "Sec-Token-Binding"
  SEC_PROVIDED_TOKEN_BINDING_ID = "Sec-Provided-Token-Binding-ID"
  SEC_REFERRED_TOKEN_BINDING_ID = "Sec-Referred-Token-Binding-ID"
  SEC_WEBSOCKET_ACCEPT = "Sec-WebSocket-Accept"
  SEC_WEBSOCKET_EXTENSIONS = "Sec-WebSocket-Extensions"
  SEC_WEBSOCKET_KEY = "Sec-WebSocket-Key"
  SEC_WEBSOCKET_PROTOCOL = "Sec-WebSocket-Protocol"
  SEC_WEBSOCKET_VERSION = "Sec-WebSocket-Version"
  CDN_LOOP = "CDN-Loop"

  @classmethod
  def list(cls):
    return list(map(lambda field: field.value, HttpHeaderFields))

  @classmethod
  def get_from_lower(cls, name):
    for field in cls:
      if field.value.lower() == name.lower():
        return field.value
