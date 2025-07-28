import httpx

users = {
   "email": "Stepan@moruch.com",
   "password": "moruch"
}

response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=users)

print(response.status_code)  # 201 (Created)
print(response.json())       # Ответ с созданной записью


access_token = ("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHBpcmUiOiIyMDI1LTA3LTI4VDE2OjE3OjA1LjUwMTgyNyIsInVzZXJfaWQiOiI"
                "1N2IyZjU3Mi1hODdkLTQ0ZTgtODg2OC1kOTBkYjAwYjY0MDAifQ.FF2GX_medvQK3LJ3zjjNhFktiE9t0AzjXaH1ZojxF2Y")

headers = {
    "Authorization": f"Bearer {access_token}"
}


response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)


print(response.status_code)
print(response.json())
