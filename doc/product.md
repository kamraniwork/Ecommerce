# Product

1. product endpoint
    *   [list](#list-product)
    *   [create](#create-category)
    *   [update](#update-category)
    *   [delete](#delete-category)

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
    "title": "راهیان ارشد سیستم عامل",
    "description": "کتاب بسیار عالی",
    "product_type": {
        "pk": 1,
        "name": "کتاب",
        "typed_product": [
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
    },
    "category": {
        "name": "کنکور",
        "slug": "konkur",
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
                    },
                    {
                        "name": "مدیریت حافظه",
                        "slug": "mhafeze",
                        "parent": 2,
                        "children": []
                    }
                ]
            }
        ]
    },
    "slug": "syskhalili",
    "regular_price": "100.00",
    "discount_price": "80.00",
    "updated_at": "2022-06-16T12:14:23.337005Z"
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