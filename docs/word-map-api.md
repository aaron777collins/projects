# word-map-api

## 🔗 Quick Links

- [View on GitHub](https://github.com/aaron777collins/word-map-api)

## 📊 Project Details

- **Primary Language:** Python
- **Languages Used:** Python, Shell, Batchfile
- **License:** None
- **Created:** May 26, 2022
- **Last Updated:** May 26, 2022

## 📝 About

# word-map-api
Takes a word array and returns the synonyms/antonyms related to each.

For example:
```
send:
{
    "words": ["Beautiful", "Cool", "collected"]
}
```
and receive:
```
{
    "beautiful": {
        "antonyms": [
            "ugly"
        ],
        "synonyms": [
            "beautiful"
        ]
    },
    "collected": {
        "antonyms": [
            "spread",
            "uncollected",
            "ungathered"
        ],
        "synonyms": [
            "take_in",

