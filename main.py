import gc
import csv
import argparse

from pymilvus import utility
from pymilvus import connections
from pymilvus import Collection

# 連接 Milvus 服務器
connections.connect(alias="default", host='localhost', port='19530')

def update(file_path:str):
    # 读取目录中的所有数据
    pass

def backup():
    # 列出所有集合
    data = utility.list_collections()
    print('列出所有集合')
    print(data)
    for item in data:
        collection = Collection(item)
        if collection.is_empty or collection.name != 'test_default':
            print('集合为空或忽略:', item)
            continue

        print('连接集合:', collection.name)
        print('集合中实体数量:', collection.num_entities)
        print('集合的schema:', collection.schema)
        #print('集合的描述:', collection.description)
        #print('集合主键字段:', collection.primary_field)
        #print('集合 list[Partition] 对象:', collection.partitions)
        #print('集合 list[index] 对象:', collection.indexes)
        n = collection.num_entities
        i = 0
        while i < n:
            print('分批写入:', i)
            with open('/data/default/default-{x}.csv'.format(x=i), 'w', encoding='utf8', newline='') as file:
                doc = csv.DictWriter(file, ['id', 'article_id', 'embedding'])
                doc.writeheader()
                x = i
                while x < i+10000:
                    print('分段写入:', x)
                    rest = collection.query(
                        expr = "id > {op} and id < {ed}".format(op=x, ed=x+100),
                        output_fields = ["id", "article_id", "embedding"],
                        consistency_level="Strong",
                    )
                    doc.writerows(rest)
                    del rest
                    gc.collect()
                    x += 100
                file.close()
            i += 10000

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-backup", type=str, required=False, help="输入备份存放路径")
    parser.add_argument("-update", type=str, required=False, help="输入读取备份路径")
    args = parser.parse_args()
    print(args.s, args.v)
    if args.s == 'backup':
        backup()
    if args.s == 'update':
        update()
    if args.s is None:
        print('可以输入参数 -s backup 备份数据')
        print('可以输入参数 -s update 恢复数据')





