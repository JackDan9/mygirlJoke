# mygirlJoke
- The project inspired by [Honglei][1] Brother.
- The project for mygirl.

------

## SetUp
```bash
## Install Python-IDE
python 2.7.14

## Install Scrapy
### upgrade pip
python -m pip install --upgrade pip
pip install Scrapy

## store project
Go to the directory where you want to store the project. like this:
C:> cd projects
C:\projects>cd workspace
C:\projects\workspace>

## git clone project
C:\projects\workspace>git clonegit@github.com:JackDan9/mygirlJoke.git
or
C:\projects\workspace>git https://github.com/JackDan9/mygirlJoke.git

## run project
Go to the project directory and run the project. like this:
C:\projects\workspace>cd mygirlJoke
C:\projects\workspace\mygirlJoke>scrapy crawl mygirlJoke

```

- [python-2.7.14][2]

------

## Description

![description][3]

- Spider the most funny data.
- The `New_Joke_Url` for "查看全文".

------

## SetEmailInfo
```
# It is receiver email word.
mailto_list = "*********@qq.com"
mail_host = "smtp.qq.com"
# It is your email word.
mail_user = "********@qq.com"
# It is your password
mail_pass = "**********"
```
- These are your own email parameters

------

## Result

![result][4]

## Thanks
- If you like it, please give me a **star**!
- This will support me to keep updating!


  [1]: https://github.com/lianghonglei
  [2]: https://www.python.org/downloads/release/python-2714/
  [3]: ./images/description.png "description.png"
  [4]: ./images/result.jpg "result.jpg"