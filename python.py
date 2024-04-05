import csv

def replace_ip(uri, new_ip):
    return uri.replace('ip地址', new_ip)

def main():
    # 读取 IP 地址列表
    ip_list = []
    with open('ip_list.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            ip_list.append(row[0])  # 假设 IP 地址在每行的第一个列

    # 给定的 VLESS 节点 URI
    vless_uri = "vless://b51454ac-dc04-43a7-950a-f4edaf5de118@ip地址:80?encryption=none&security=none&sni=warp.jerryyu2022.workers.dev&type=ws&host=warp.jerryyu2022.workers.dev&path=%2F%3Fed%3D2048#node"

    # 打开一个文本文件用于写入节点 URI
    with open('output_nodes.txt', 'w') as output_file:
        # 替换 IP 地址并输出所有节点
        for ip in ip_list:
            replaced_uri = replace_ip(vless_uri, ip)
            output_file.write(replaced_uri + '\n')
    
    print("输出结束")

if __name__ == "__main__":
    main()
