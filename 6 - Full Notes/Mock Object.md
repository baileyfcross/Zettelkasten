2026-09-06 20:37

Status: #baby

Tags: [[Web Application Testing]] [[React Testing Practice]] [[R Software Testing]]

# Mock Object

A mock object replaces a real dependency with controlled behavior during a test. It can return prepared values and record interactions without contacting a database, network service, or other external system.

ASP.NET Core tests can mock a [[Database Context]], while Angular tests can provide a fake [[Angular Service]]. The unit under test then runs predictably and failures remain focused on its own behavior.

In the React examples, a mock function records whether a click callback was invoked, while a mocked component replaces a child that is outside the test's scope. Jest can define the replacement inline or load a manual mock module, allowing a container or parent component to be exercised without depending on the real child's rendering.

In R database tests, a mock can replace the connection, the connection wrapper, or the domain-specific query function. Moving the replacement higher makes the test faster and more portable, but removes more production behavior from the evidence. [[R Database Test Mocking]] therefore chooses the boundary according to whether the test is meant to verify database access, query construction, or downstream analysis.

# References

[[aspnetcore3andangular9_3ed.pdf]]

[[learningreact1.pdf]]

[[testingrcode.pdf]]
