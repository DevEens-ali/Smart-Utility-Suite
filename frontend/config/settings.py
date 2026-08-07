"""
Global application settings.

Keeping page config and theme colors in one place makes it easy to
re-skin the app or add new pages later without touching UI code.
"""

# ---- Page config -----------------------------------------------------
PAGE_TITLE = "UtilityHub"
PAGE_ICON = "🧮"  # only used for the browser tab, not shown in the UI
LAYOUT = "wide"
SIDEBAR_STATE = "expanded"

# ---- App branding ------------------------------------------------------
APP_NAME = "UtilityHub"

# ---- Theme colors (match the reference design) ------------------------
COLORS = {
    "primary_blue": "#2563EB",
    "primary_blue_light": "#3B82F6",
    "sidebar_bg": "#FAFBFC",
    "content_bg": "#FFFFFF",
    "active_bg": "#EFF6FF",
    "text_dark": "#111827",
    "text_gray": "#6B7280",
    "text_muted": "#9CA3AF",
    "border_color": "#E5E7EB",
    "icon_default": "#374151",
}
