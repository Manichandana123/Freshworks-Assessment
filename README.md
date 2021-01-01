# A file-based datastore that supports basic CRD operations(CREATE,READ,DELETE)

The data store will support the following :

It can be initialized using an optional file path. If one is not provided, it will reliably create itself in a reasonable location on the laptop.
A new key-value pair can be added to the data store using the Create operation. The key is always a string - capped at 32chars. The value is always a JSON object - capped at 16KB.
If Create is invoked for an existing key, an appropriate error must be returned.
A Read operation on a key can be performed by providing the key, and receiving the value in response, as a JSON object.
A Delete operation can be performed by providing the key.
Every key supports setting a Time-To-Live property when it is created. This property is optional. If provided, it will be evaluated as an integer defining the number of seconds the key must be retained in the data store. Once the Time-To-Live for a key has expired, the key will no longer be available for Read or Delete operations.
Appropriate error responses must always be returned to a client if it uses the data store in unexpected ways or breaches any limits
The file size never exceeds 1GB

Go through the code.py file to know about CRD operations and data_df.json file stores the data.
Initially,if a client want to create a key,client must give key value pair as input whereas time-to-live property is optional

![Screenshot (216)](https://user-images.githubusercontent.com/58383104/103439215-fb341d00-4c60-11eb-9846-1e4b85ca1eba.png)

