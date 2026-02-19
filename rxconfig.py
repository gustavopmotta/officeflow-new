import reflex as rx

config = rx.Config(
    app_name="officeflow_new",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)