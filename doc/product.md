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
