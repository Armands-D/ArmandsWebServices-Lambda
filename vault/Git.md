# Init
**Great Resource:** https://www.datacamp.com/tutorial/git-init
```bash
git init
```

## Connect Remote & Local Repo
- `<repository-url>` can be HTTPS or SSH
	- Can be changed later
```bash
git remote add origin <>
git remote -v # Verify connection
```

### Change Repo URL
- Authentication & Access
- Replace with SSH or HTTPS url
```bash
git remote set-url origin git@github.com:your-username/your-repo.git
```

# Push Commit & Branch Track Remote
- A commit is required to push
- we push upstream to remote origin branch master
	- May cause merge conflict
```bash
git push -u origin $(git branch --show-current)  # Works for 'main' or 'master' 
```
