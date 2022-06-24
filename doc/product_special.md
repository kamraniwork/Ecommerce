# Product Special

1. product_special endpoint
    *   [create](#create-product_special)
    *   [update](#update-product_special)
    
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