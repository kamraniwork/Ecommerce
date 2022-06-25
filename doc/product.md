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
