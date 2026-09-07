2026-09-06 20:52

Status: #baby

Tags: [[Redux State Management]]

# Redux Thunk

Redux Thunk is middleware that lets dispatch accept a function in addition to a plain action object. That function receives dispatch and can perform asynchronous work before sending ordinary actions to the reducer.

In an API workflow, a thunk can dispatch a request action, await the response, and then dispatch either success or failure. The reducer remains synchronous even though the wider operation spans time.

# References

[[aspnetcore3andreact.pdf]]
