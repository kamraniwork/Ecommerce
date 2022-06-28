# Product

1. product endpoint
    *   [list](#list-product)
    *   [create](#create-product)
    *   [update](#update-product)
    *   [delete](#delete-product)

### list product
*   ###### Description: 
       return all product object that `is_active==True`
* ###### Request: `GET`  `http://localhost:8000/product/`
* ###### Param: `None`
* ###### Response:
```json
[
    {
        "title": "راهیان ارشد سیستم عامل",
        "slug": "syskhalili",
        "regular_price": "100.00",
        "discount_price": "80.00",
        "updated_at": "2022-06-16T12:14:23.337005Z"
    }
]
```
## retrieve product
*   ###### Description: 
       return product object that `is_active==True` with category and product_type
* ###### Request: `GET`  `http://localhost:8000/product/{slug}`
* ###### Param: `slug`
* ###### Response:
```json
{
    "title": "A51",
    "description": "mobile A51",
    "product_type": {
        "pk": 2,
        "name": "mobile",
        "typed_product": [
            {
                "pk": 3,
                "name": "os",
                "special_value_product": [
                    {
                        "pk": 1,
                        "value": "mx150"
                    },
                    {
                        "pk": 3,
                        "value": "android"
                    }
                ]
            },
            {
                "pk": 4,
                "name": "ram",
                "special_value_product": [
                    {
                        "pk": 4,
                        "value": "128"
                    }
                ]
            }
        ]
    },
    "category": {
        "name": "mobile",
        "slug": "mobile",
        "parent": 5,
        "children": []
    },
    "slug": "a51",
    "regular_price": "100.00",
    "discount_price": "80.00",
    "updated_at": "2022-06-28T09:07:12.706998Z"
}
```
## create product
* ###### Description: 
    jsut superuser can create new product object
    
* ###### Request: `post`  `http://localhost:8000/product/`
* ###### Param:
    *   `title`: required | ![](https://img.shields.io/static/v1?label=&message=string&color=red)
    *   `slug`: required | ![](https://img.shields.io/static/v1?label=&message=string&color=red)
    *   `regular_price`: required | ![](https://img.shields.io/static/v1?label=&message=decimal&color=red)
    *   `discount_price`: required | ![](https://img.shields.io/static/v1?label=&message=decimal&color=red)
    *   `description`: not required | ![](https://img.shields.io/static/v1?label=&message=string&color=red)
    *   `is_active`: auto False | ![](https://img.shields.io/static/v1?label=&message=boolean&color=red)
    *   `product_type_name`: required | ![](https://img.shields.io/static/v1?label=&message=string&color=red)
    *   `category_name`: required | ![](https://img.shields.io/static/v1?label=&message=string&color=red)
* ###### example:
```json
{
   "title": "test",
   "slug": "test",
   "regular_price": "100.00",
   "discount_price": "80.00",
   "description":"test",
   "is_active":"true",
   "product_type_name":"کتاب",
   "category_name":"کنکور"
}
```
* ###### response:
    if OK request:
    `status=200`
    ```json
      {"status": "create product object successfully"}
    ```
    else if there is error:
    `status=400`
    ```json
    {
        "title": [
            "This field is required."
        ],
        "slug": [
            "This field is required."
        ]
    }
    ```
  
## update product
* ###### Description: 
    jsut superuser can update product object
    
* ###### Request: `put`  `http://localhost:8000/product/{slug}`
* ###### Param:
    *   `title`: required | ![](https://img.shields.io/static/v1?label=&message=string&color=red)
    *   `slug`: required | ![](https://img.shields.io/static/v1?label=&message=string&color=red)
    *   `regular_price`: required | ![](https://img.shields.io/static/v1?label=&message=decimal&color=red)
    *   `discount_price`: required | ![](https://img.shields.io/static/v1?label=&message=decimal&color=red)
    *   `description`: not required | ![](https://img.shields.io/static/v1?label=&message=string&color=red)
    *   `is_active`: auto False | ![](https://img.shields.io/static/v1?label=&message=boolean&color=red)
    *   `product_type_name`: required | ![](https://img.shields.io/static/v1?label=&message=string&color=red)
    *   `category_name`: required | ![](https://img.shields.io/static/v1?label=&message=string&color=red)
* ###### example:
```json
{
   "title": "test3",
   "slug": "test",
   "regular_price": "100.00",
   "discount_price": "80.00",
   "description":"test",
   "is_active":"true",
   "product_type_name":"کتاب",
   "category_name":"کنکور"
}
```
* ###### response:
    if OK request:
    `status=200`
    ```json
      {"status": "update product"}
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
## delete product
* ###### Description: 
    delete product object by slug field
    
* ###### Request: `delete`  `http://localhost:8000/product/{slug}`
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