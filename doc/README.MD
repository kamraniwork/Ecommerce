# ECOMMERCE 

1. [run project](#run-project)
    *   [requirements](#requirements)
    *   [Database for product model](#database-for-product-model)
2. [tests](#tests)
    *   [coverage](#use-coverage)
3. [endpoints](#endpoints)
4. [security](#security)

## Run Project
* ###### Requirements:
     I use `pipreqs ` library for create requirements.txt
     ```text
      pip install pipreqs
      pipreqs my_path
     ```
     If this file already exists, you must use:
     ```text
      pipreqs --encoding=utf8 --force .
     ```
* ###### Database for product model
    use `https://vuerd.github.io/` website
    ```mariadb
      CREATE TABLE category(
          name        CHAR    NULL     COMMENT 'Required and unique',
          slug        CHAR    NULL     COMMENT 'Required and unique',
          is_active   BOOLEAN NULL     DEFAULT true,
          category_id INT     NOT NULL COMMENT 'Many to many field',
          PRIMARY KEY (category_id)
      );
      
      CREATE TABLE Product(
          title           CHAR     NULL     COMMENT 'Required',
          description     TEXT     NULL     COMMENT 'Not Required',
          slug            CHAR     NULL     COMMENT 'Required',
          Regular_price   DECIMAL  NULL    ,
          discount_price  DECIMAL  NULL    ,
          is_active       BOOLEAN  NULL     DEFAULT true,
          created_at      DATETIME NULL    ,
          updated_at      DATETIME NULL    ,
          product_type_id INT      NOT NULL,
          category_id     INT      NOT NULL COMMENT 'Many to many field',
          product_id      INT      NOT NULL,
          PRIMARY KEY (product_id)
    );
    
      CREATE TABLE ProductImage(
          image      CHAR    NULL    ,
          product_id INT      NOT NULL,
          alt_text   CHAR     NULL    ,
          is_feature BOOLEAN  NULL    ,
          created_at DATETIME NULL    ,
          updated_at DATETIME NULL    
    );
      
      CREATE TABLE ProductSpecification(
          product_type_id          INT  NULL     COMMENT 'ForeignKey',
          name                     CHAR NULL     COMMENT 'Required',
          id                       INT  NOT NULL,
          product_specification_id INT  NOT NULL,
          PRIMARY KEY (product_specification_id)
    );
      CREATE TABLE ProductSpecificationValue(
          product_id               INT  NOT NULL,
          product_specification_id INT  NOT NULL,
          value                    CHAR NULL    
    );
      CREATE TABLE ProductType(
      name            CHAR    NULL     COMMENT 'Required',
      is_active       BOOLEAN NULL     DEFAULT true,
      product_type_id INT     NOT NULL,
      PRIMARY KEY (product_type_id)
    );
    ```
    and use `https://asciiflow.com/` for:
    ```text
         ┌─────────────────────┐
         │                     │
         │                   ┌─┼─┐
    ┌────┴────────┐      ┌───┴─┼─┴────┐  xxxxx       xxxxxx
    │             │      │     │      │ xx   xx   xxxx   xx
    │             │      │  product   │ x     xxxxx      xx
    │             │      │            │xx       x        xx
    │    product  │      │  image     │ x               xx
    │             │      │            │ xx             xxx
    │             │      │  alt_text  │  xxx           xx
    │             │      │            │   xx          xx
    │             │      │  is_feature│     xx       xx
    │             │      │            │      xxx    xx
    │             │      │  create_at │        xxxxx
    └─────────────┘      └────────────┘          xx
    ```
  
## tests
* ###### use coverage:
     I use coverage package for measure the quality of the test:
     ```text
      coverage run manage.py test
      coverage report -m
     ```
    for dont check Extra files must:
    ```text
      coverage run —omit='*/venv/*' manage.py test
    ```

## endpoints
### list category
*   ###### Description: 
       return many nested category object that `is_active==True`
* ###### Request: `GET`  `http://localhost:8000/category/`
* ###### Param: `None`
* ###### Response:
```json
[
    {
        "name": "کنکور",
        "slug": "nor",
        "parent": null,
        "children": [
            {
                "name": "سیستم عامل",
                "slug": "sstm-aaml",
                "parent": 1,
                "children": [
                    {
                        "name": "مدیریت دیسک",
                        "slug": "mdrt-ds",
                        "parent": 2,
                        "children": []
                    }
                ]
            }
        ]
    }
]
```
## create category
* ###### Description: 
    jsut superuser can create new category object
    
* ###### Request: `post`  `http://localhost:8000/category/`
* ###### Param:
    *   `name`: required | ![](https://img.shields.io/static/v1?label=&message=string&color=red)
    *   `slug`: required | ![](https://img.shields.io/static/v1?label=&message=string&color=red)
    *   `parent_name`: required | ![](https://img.shields.io/static/v1?label=&message=string&color=red)
* ###### example:
```json
{
    "name":"مدیریت حافظه",
    "slug":"mhafeze",
    "parent_name":"سیستم عامل"
}
```
* ###### response:
    if OK request:
    `status=200`
    ```json
      {"status": "create category object successfully"}
    ```
    else if there is error:
    `status=400`
    ```json
    {
        "name": [
            "This field is required."
        ],
        "slug": [
            "This field is required."
        ]
    }
    ```
  
## update category
* ###### Description: 
    jsut superuser can update category object
    
* ###### Request: `put`  `http://localhost:8000/category/{slug}`
* ###### Param:
    *   `name`: not required | ![](https://img.shields.io/static/v1?label=&message=string&color=red)
    *   `slug`: not required | ![](https://img.shields.io/static/v1?label=&message=string&color=red)
    *   `parent_name`: not required | ![](https://img.shields.io/static/v1?label=&message=string&color=red)
* ###### example:
```json
{
    "name":"مدیریت حافظه",
    "slug":"mhafeze",
    "parent_name":"سیستم عامل"
}
```
* ###### response:
    if OK request:
    `status=200`
    ```json
      {
        "name":"مدیریت حافظه",
        "slug":"mhafeze",
        "parent_name":"سیستم عامل"
      }
    ```
    else if there is error:
    `status=400`
    ```json
    {
        "name": [
            "This field is required."
        ],
        "slug": [
            "This field is required."
        ]
    }
    ```
## delete category
* ###### Description: 
    delete category object by slug field
    
* ###### Request: `delete`  `http://localhost:8000/category/{slug}`
* ###### Param: `None`
* ###### response:
    if OK request:
    `status=200`
    ```json
      {"status": "deleted object"}
    ```
    else if there is error:
    `status=404`
    ```json
    {
        "status":"Not found"
    }
    ```
## list product_type
*   ###### Description: 
       return product_type object that `is_active==True`
* ###### Request: `GET`  `http://localhost:8000/product-type/`
* ###### Param: `None`
* ###### Response:
```json
[
    {
        "name": "کتاب"
    }
]
```
## retrieve product_type
*   ###### Description: 
       return product_type object that `is_active==True` with product_specification list
* ###### Request: `GET`  `http://localhost:8000/product-type/{pk}`
* ###### Param: `pk`
* ###### Response:
```json
{
    "pk": 1,
    "name": "کتاب",
    "typed_product": [
        {
            "pk": 1,
            "name": "نویسنده"
        },
        {
            "pk": 2,
            "name": "قیمت"
        },
        {
            "pk": 3,
            "name": "تعداد صفحه"
        },
        {
            "pk": 4,
            "name": "تعداد فصل"
        }
    ]
}
```
## create product_type
* ###### Description: 
    jsut superuser can create new product_type object
    
* ###### Request: `post`  `http://localhost:8000/product-type/`
* ###### Param:
    *   `name`: required | ![](https://img.shields.io/static/v1?label=&message=string&color=red)
    *   `is_active`: required | ![](https://img.shields.io/static/v1?label=&message=string&color=red)

* ###### example:
```json
{
    "name":"لوازم دیجیتال",
    "is_active": "true"
}
```
* ###### response:
    if OK request:
    `status=200`
    ```json
      {"status": "create product_type object successfully"}
    ```
    else if there is error:
    `status=400`
    ```json
    {
        "name": [
            "This field is required."
        ]
    }
    ```
  
## update product_type
* ###### Description: 
    jsut superuser can update product_type object
    
* ###### Request: `put`  `http://localhost:8000/product-type/{pk}`
* ###### Param:
    *   `name`: not required | ![](https://img.shields.io/static/v1?label=&message=string&color=red)
    *   `is_active`: not required | ![](https://img.shields.io/static/v1?label=&message=string&color=red)
  
* ###### example:
```json
{
    "name":"لوازم دیجیتال",
    "is_active": "true"
}
```
* ###### response:
    if OK request:
    `status=200`
    ```json
    {
      "name":"لوازم دیجیتال",
      "is_active": "true"
    }
    ```
    else if there is error:
    `status=400`
    ```json
    {
        "name": [
            "This field is required."
        ]
    }
    ```
## delete product_type
* ###### Description: 
    delete product_type object by pk field
    
* ###### Request: `delete`  `http://localhost:8000/product-type/{pk}`
* ###### Param: `None`
* ###### response:
    if OK request:
    `status=200`
    ```json
      {"status": "deleted object"}
    ```
    else if there is error:
    `status=404`
    ```json
    {
        "status":"Not found"
    }
    ```
  
## create product_special
* ###### Description: 
    jsut superuser can create new product_special object
    
* ###### Request: `post`  `http://localhost:8000/product-specification/`
* ###### Param:
    *   `name`: required | ![](https://img.shields.io/static/v1?label=&message=string&color=red)
    *   `product_type_name`: required | ![](https://img.shields.io/static/v1?label=&message=string&color=red)

* ###### example:
```json
{
    "name":"باتری",
    "product_type_name":"لوازم دیجیتال"
}
```
* ###### response:
    if OK request:
    `status=200`
    ```json
      {"status": "create product_special object successfully"}
    ```
    elif there is error:
    `status=400`
    ```json
    {
        "name": [
            "This field is required."
        ]
    }
    ```
    else `status=404`
    ```json
    {
      "detail": "Not found."
    }
    ```
## update product_special
* ###### Description: 
    jsut superuser can update product_special object
    
* ###### Request: `put`  `http://localhost:8000/product-specification/{name}`
* ###### Param:
    *   `name`: not required | ![](https://img.shields.io/static/v1?label=&message=string&color=red)
    *   `product_type_name`: required | ![](https://img.shields.io/static/v1?label=&message=string&color=red)
  
* ###### example:
```json
{
    "name":"تعداد صفحات",
    "product_type_name": "کتاب"
}
```
* ###### response:
    if OK request:
    `status=200`
    ```json
    {
    "name":"تعداد صفحات",
    "product_type_name": "کتاب"
    }
    ```
    elif there is error:
    `status=400`
    ```json
    {
        "name": [
            "This field is required."
        ]
    }
    ```
  else `status=404`
    ```json
    {
      "detail": "Not found."
    }
    ```
## update product_type
* ###### Description: 
    jsut superuser can update product_type object
    
* ###### Request: `put`  `http://localhost:8000/product-type/{pk}`
* ###### Param:
    *   `name`: not required | ![](https://img.shields.io/static/v1?label=&message=string&color=red)
    *   `is_active`: not required | ![](https://img.shields.io/static/v1?label=&message=string&color=red)
  
* ###### example:
```json
{
    "name":"لوازم دیجیتال",
    "is_active": "true"
}
```
* ###### response:
    if OK request:
    `status=200`
    ```json
    {
      "name":"لوازم دیجیتال",
      "is_active": "true"
    }
    ```
    else if there is error:
    `status=400`
    ```json
    {
        "name": [
            "This field is required."
        ]
    }
    ```
## delete product_type
* ###### Description: 
    delete product_type object by pk field
    
* ###### Request: `delete`  `http://localhost:8000/product-type/{pk}`
* ###### Param: `None`
* ###### response:
    if OK request:
    `status=200`
    ```json
      {"status": "deleted object"}
    ```
    else if there is error:
    `status=404`
    ```json
    {
        "status":"Not found"
    }
    ```
## security
* ###### use throttling:
user can not more than 3 each per second
and use to Viewsets class in views.py file:
```python
from pytimeparse.timeparse import timeparse
from rest_framework.throttling import UserRateThrottle

class CustomThrottlingUser(UserRateThrottle):
    scope = 'apps'
    rate = '3/1s'

    def parse_rate(self, rate):

        if rate is None:
            return None, None
        num, period = rate.split('/')
        num_requests = int(num)
        duration = timeparse(period)
        return num_requests, duration

def get_throttles(self):

    throttle_classes = (CustomThrottlingUser,)
    return [throttle() for throttle in throttle_classes]
```
