# Product Type

1. product_type endpoint
    *   [list](#list-product_type)
    *   [create](#create-product_type)
    *   [update](#update-product_type)
    *   [delete](#delete-product_type)
    *   [retrieve](#retrieve-product_type)
    
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