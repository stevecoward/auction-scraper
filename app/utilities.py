import datetime
import decimal

def result_to_list(rows):
    """ ResultProxy to json-serializable array helper """
    prepared = []
    for row in rows:
        mutated = {}
        for key, item in dict(row).iteritems():
            if isinstance(item, decimal.Decimal):
                item = float(item)
            if isinstance(item, datetime.date):
                item = '%s' % item
            mutated[key] = item
        prepared.append(mutated)
    return prepared

def request_to_dict(values):
    result = {}
    for k, v in values.iteritems():
        result[k] = v
    return result
