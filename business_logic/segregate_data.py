def segregate_data(data):
    citywise_data={}
    for subdata in data:
        if subdata['city'] not in citywise_data:
            citywise_data[subdata['city']]=[]
            citywise_data[subdata['city']].append(subdata)
        else:
            citywise_data[subdata['city']].append(subdata)
    return citywise_data


