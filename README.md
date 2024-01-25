# Persian Names

A json file contains 8816 persian name with their gender (some of them is not labeled)

# اسامی ایرانی

یک فایل json که حاوی ۸۸۱۶ نام ایرانی به همراه جنسیت آنها (برخی از اسامی بدون برچسب جنسیت هستند) می‌باشد.

## Resource (منابع)

- <http://rastan.parsiblog.com/posts/271>
- <https://www.kaggle.com/datasets/hamedetezadi/persianfarsi-names-dataset>

## Description

I just download 2 xls and csv files from the internet, then preprocessed them to make the data of the two files compatible and finally merge them into one json file.

### Preprocess

1. removeing arabic standard characters that are not in persian words, like `ئ` or ‍‍`ك`
2. removing arabic irabs from words, like `ـَـِـُ`

## توضیحات

بنده دو فایل اکسل و csv که از اینترنت پیدا کردم را ابتدا با استفاده از پردازش‌های ساده‌ با یکدیگر سازگار کرده سپس داده‌های دو فایل را با هم ادغام کردم.

### پیش‌پردازش‌ها

1. حذف حروف استاندارد عربی مانند `ئ` و `ك`
2. حذف اعراب از اسامی مانند `ـَـِـُ`

## Todos

- [x] parse and merge two name files
- [ ] add missing genders to rest of the names
- [ ] add names latin version to the results
- [ ] add names pronounciations (maybe in audio format) to the results
