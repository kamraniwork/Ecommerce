# Category

1. category endpoint
    *   [list](#list-category)
    *   [create](#create-category)
    *   [update](#update-category)
    *   [delete](#delete-category)

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