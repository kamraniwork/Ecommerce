# Product Image

1. Product Image endpoint
    * [list](#list-category)
    * [create](#create-category)
    * [update](#update-category)
    * [delete](#delete-category)

### list product image

*   ###### Description:
    return all image objects
* ###### Request: `GET`  `http://localhost:8000/images/`
* ###### Param: `None`
* ###### Response:

```json
[
  {
    "pk": 1,
    "image": "http://localhost:8000/media/images/Screenshot_from_2022-06-28_04-31-15.png",
    "alt_text": null
  },
  {
    "pk": 2,
    "image": "http://localhost:8000/media/images/Screenshot_from_2022-06-28_04-31-15.png",
    "alt_text": null
  },
  {
    "pk": 3,
    "image": "http://localhost:8000/media/images/Screenshot_from_2022-06-28_12-54-46_SLnTCw9.png",
    "alt_text": "main picture"
  }
]
```

## create product image

* ###### Description:
  jsut superuser can create new object

* ###### Request: `post`  `http://localhost:8000/images/`
* ###### Param:
    * `product_slug`: required | ![](https://img.shields.io/static/v1?label=&message=string&color=red)
    * `image`: required | ![](https://img.shields.io/static/v1?label=&message=string&color=red)
    * `alt_text`: required | ![](https://img.shields.io/static/v1?label=&message=string&color=red)
    * `is_feature`: not required | ![](https://img.shields.io/static/v1?label=&message=boolean&color=red)
* ###### example:

```json
{
  "product_slug": "samsung-a51",
  "alt_text": "main image",
  "image": ImageFile
}
```

* ###### response:
  if OK request:
  `status=200`
    ```json
      {"status": "create product_image object successfully"}
    ```
  else if there is error:
  `status=400`
    ```json
    {
        "image": [
            "This field is required."
        ],
        "product_slug": [
            "This field is required."
        ],
        "alt_text": [
            "This field is required."
        ]
    }
    ```
  else if there is not product with slug ==> `status=404`

## update product

* ###### Description:
  jsut superuser can update object

* ###### Request: `put`  `http://localhost:8000/images/{pk}`
* ###### Param:
    * `product_slug`: required | ![](https://img.shields.io/static/v1?label=&message=string&color=red)
    * `image`: required | ![](https://img.shields.io/static/v1?label=&message=string&color=red)
    * `alt_text`: required | ![](https://img.shields.io/static/v1?label=&message=string&color=red)
    * `is_feature`: not required | ![](https://img.shields.io/static/v1?label=&message=boolean&color=red)
* ###### example:

```json
{
  "product_slug": "samsung-a51",
  "alt_text": "my image",
  "image": ImageFile
}
```

* ###### response:
  if OK request:
  `status=200`
    ```json
  {
  "status": "update object"
  }
    ```
  else if there is error:
  `status=400`
    ```json
    {
        "image": [
            "This field is required."
        ],
        "product_slug": [
            "This field is required."
        ],
        "alt_text": [
            "This field is required."
        ]
    }
    ```

## delete image

* ###### Description:
  delete productImage object by pk field

* ###### Request: `delete`  `http://localhost:8000/images/{pk}`
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