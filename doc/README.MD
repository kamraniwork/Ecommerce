# ECOMMERCE 

1. [run project](#run-project)
2. [tests](#tests)

## Run Project
* ###### Requirements:
     I use `pipreqs ` library for create requirements.txt
     ```text
      pip install pipreqs
      pipreqs my_path
     ```
     If this file already exists, you must use:
     ```text
      pipreqs --force
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