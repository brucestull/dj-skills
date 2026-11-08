# dj-skills

A tiny reusable Django app. It provides one model, `Skill`, where each skill
belongs to a user — so a user can have many skills.

## Install (from GitHub, pinned to a tag)

```
uv add "git+https://github.com/brucestull/dj-skills.git@v0.1.0"
```

## Enable it

Add the app to `INSTALLED_APPS` (note the underscore — the import name is
`dj_skills`, not `dj-skills`):

```python
INSTALLED_APPS = [
    # ...
    "dj_skills",
]
```

Then run migrations:

```
python manage.py migrate
```

## What you get

- A `Skill` model: `name`, `description`, and a `user` foreign key
  (`settings.AUTH_USER_MODEL`, `related_name="skills"`).
- `Skill` registered in the Django admin.

## The model

```python
class Skill(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="skills",
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
```

Access a user's skills with `user.skills.all()`.
