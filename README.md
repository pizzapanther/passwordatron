# Passwordatron

*Insecure way to secure your applications*

A small utility that requires a password before starting an application. Let's you limit access to applications on a shared computer. Note, anyone with some tech skills will find a way around this. Think of it as a door to let people know not use that application.

## Configuration File

```json
{
  "password": "super-insecure-way-of-storing-a-password",
  "app-name1": "/path/to/application add-some-args --like-this",
  "app-name2": "/path/to/another/application add-some-args --like-this"
}
```
