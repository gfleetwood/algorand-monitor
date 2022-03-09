# Algorand Monitor

A project to track the price of the Algorand cryptocurrency. **Dagster** orchestrates the ELT process run every minute via cron. Data comes from the **Coinmarket Cap API** which is stored directly in a **Postgres** database. The price data is displayed using a R Shiny app. Everything besides the databases is packaged in **docker** containers managed by **docker compose**.
