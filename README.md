# About
[Spring Cloud Vault](https://cloud.spring.io/spring-cloud-vault/) is used to build an application that retrieves its configuration properties from HashiCorp [Vault](https://www.vaultproject.io/). [(See the guide)](https://spring.io/guides/gs/vault-config/)

This script can be used to read values of properties from vault and use them as (default) values in a Spring boot *application.properties* file. Keeping your *application.properties* up-to-date is usefull for local tests and for the situation in which the connection to vault is lost.
# Usage
```
python vault_to_properties.py [secret-address] [application.properties file address]  [vault token]
```
- \[secret-address\] is something like https://your-vault-address.com/v1/secret/data/service-name/env.
- \[*application.properties* file address\] is the address to spring boot *application.properties* file which is used to write default values on. (the file won't be replaced and a new file is made based on this one)
- \[vault token\] is the token of the vault you are trying to read values from. It is like "s.XXXXXXXXXXXXXXXXXXXXXXXX" and can be found in header of requests to vault (e.g. in browser).
# Output
The values retrieved from vault will be printed on console and the new *application.properties* file is generated in current working directory.