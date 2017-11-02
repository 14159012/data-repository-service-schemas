# With app.py running start this demo
import client

models = client.models
client = client.client


def client_demo():
    # CreateDataObject
    print("..........Create an object............")
    Checksum = models.get_model('ga4ghChecksum')
    URL = models.get_model('ga4ghURL')
    CreateDataObjectRequest = models.get_model('ga4ghCreateDataObjectRequest')
    DataObject = models.get_model('ga4ghCreateDataObjectRequest')
    create_data_object = DataObject(
        file_name="abc",
        checksums=[Checksum(checksum="def", type="md5")],
        urls=[URL(url="a"), URL(url="b")])
    create_request = CreateDataObjectRequest(data_object=create_data_object)
    create_response = client.CreateDataObject(body=create_request).result()
    data_object_id = create_response['data_object_id']
    print(data_object_id)

    # GetDataObject
    print("..........Get the Object we just created..............")
    get_object_response = client.GetDataObject(
        data_object_id=data_object_id).result()
    data_object = get_object_response.data_object
    print(data_object)

    # UpdateDataObject
    print("..........Update that object.................")
    UpdateDataObjectRequest = models.get_model('ga4ghUpdateDataObjectRequest')
    update_data_object = DataObject(
        file_name="abc",
        checksums=[Checksum(checksum="def", type="md5")],
        urls=[URL(url="a"), URL(url="b"), URL(url="c")])
    update_request = UpdateDataObjectRequest(data_object=update_data_object)
    update_response = client.UpdateDataObject(
        data_object_id=data_object_id, body=update_request).result()
    updated_object = client.GetDataObject(
        data_object_id=update_response['data_object_id']).result()
    print(updated_object)

    # Get the old DataObject
    print("..........Get the old Data Object.................")
    old_data_object = client.GetDataObject(
        data_object_id=update_response['data_object_id'],
        version=data_object.version).result().data_object
    print(old_data_object)

    # ListDataObjects
    print("..........List Data Objects...............")
    ListDataObjectsRequest = models.get_model('ga4ghListDataObjectsRequest')
    list_request = ListDataObjectsRequest()
    list_response = client.ListDataObjects(body=list_request).result()
    print(list_response)

    # List all versions of a DataObject
    print("..........List all Versions...............")
    versions_response = client.GetDataObjectVersions(
        data_object_id=old_data_object.id).result()
    print(versions_response)

    # DeleteDataObject
    print("..........Delete the Object...............")
    delete_response = client.DeleteDataObject(
        data_object_id=data_object_id).result()
    print(delete_response)
    try:
        client.GetDataObject(
            data_object_id=update_response['data_object_id']).result()
    except Exception as e:
        print('The object no longer exists, 404 not found. {}'.format(e))

    # CreateDataBundle

    # GetDataBundle

    # UpdateDataBundle

    # ListDataBundles

    # DeleteDataBundle


if __name__ == '__main__':
    client_demo()
