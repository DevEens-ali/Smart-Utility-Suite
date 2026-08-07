"""
Sidebar menu configuration.

This file is the single source of truth for what appears in the sidebar.
To add a new tool later (e.g. Currency Converter, PDF Tools), you only
need to add an entry here - no changes are needed in components/sidebar.py.

Icon names come from the Bootstrap Icons set (used by streamlit-option-menu).
Full icon reference: https://icons.getbootstrap.com/
"""

# The standalone "Home" entry, rendered above all sections.
HOME_ITEM = {"label": "Home", "icon": "house-door"}

# Each section is a titled group of tools in the sidebar.
# Currently only "Calculators" is active, per current requirements.
# Future sections (Converters, More Tools, AI Tools, Weather Tools, etc.)
# can simply be appended to this list.
MENU_SECTIONS = [
    {
        "title": "CALCULATORS",
        "items": [
            {"label": "Basic Calculator", "icon": "calculator"},
            {"label": "Scientific Calculator", "icon": "graph-up"},
            {"label": "CGPA Calculator", "icon": "mortarboard"},
            {"label": "GPA Calculator", "icon": "book"},
            {"label": "BMI Calculator", "icon": "heart-pulse"},
            {"label": "Age Calculator", "icon": "person"},
            {"label": "Percentage Calculator", "icon": "percent"},
        ],
    },
    # -----------------------------------------------------------------
    # Example of how future sections can be added (kept commented out
    # since they are out of scope for the current build):
    #
    # {
    #     "title": "CONVERTERS",
    #     "items": [
    #         {"label": "Currency Converter", "icon": "currency-dollar"},
    #         {"label": "Unit Converter", "icon": "rulers"},
    #         {"label": "Temperature Converter", "icon": "thermometer-half"},
    #     ],
    # },
    # {
    #     "title": "MORE TOOLS",
    #     "items": [
    #         {"label": "PDF Tools", "icon": "file-earmark-text"},
    #         {"label": "Image Tools", "icon": "image"},
    #         {"label": "Other Tools", "icon": "grid"},
    #     ],
    # },
    # -----------------------------------------------------------------
]
