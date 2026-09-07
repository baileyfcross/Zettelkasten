2026-09-06 20:31

Status: #baby

Tags: [[ASP.NET Core Application Architecture]]

# HTTP Request Pipeline

The HTTP request pipeline is the ordered path through which an ASP.NET Core application processes a request. Each registered [[ASP.NET Core Middleware|middleware]] receives an opportunity to handle the request or pass it onward.

In a combined ASP.NET Core and Angular application, the pipeline may check static resources first, then mapped API endpoints, and finally an SPA fallback. Changing the order can therefore change which layer receives the same URL.

# References

[[aspnetcore3andangular9_3ed.pdf]]
