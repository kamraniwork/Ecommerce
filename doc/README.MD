# ECOMMERCE 

1. [run project](#run-project)
    *   [requirements](#requirements)
    *   [Database for product model](#database-for-product-model)
2. [tests](#tests)
    *   [coverage](#use-coverage)
3. [endpoints](#endpoints)

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