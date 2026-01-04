# gitconfig-aliases

## 🔗 Quick Links

- [View on GitHub](https://github.com/aaron777collins/gitconfig-aliases)

## 📊 Project Details

- **Primary Language:** None
- **Languages Used:** Not specified
- **License:** None
- **Created:** November 22, 2023
- **Last Updated:** November 22, 2023

## 📝 About

# gitconfig-aliases
My git config aliases

Running the following command should add the new aliases in your .gitconfig file:
```bash
cp ~/.gitconfig ~/.gitconfig.backup && \
(grep "\[alias\]" ~/.gitconfig > /dev/null || echo -e "\n[alias]" >> ~/.gitconfig) && \
curl -s https://raw.githubusercontent.com/aaron777collins/gitconfig-aliases/main/.gitconfig | \
sed -n '/^\[alias\]/,/^$/p' | \
grep -v "^\[alias\]" >> ~/.gitconfig
```

Note that this assumes your aliases are at the bottom of the file. Y

