echo "stop firewall ..."
# systemctl stop firewalld
echo "firewall stoped ..."

sleep 1

echo "start docker ..."
# systemctl start docker
echo "docker started ..."

sleep 1

echo "start mysql ..."
docker start 33e341251685
echo "mysql started ..."

sleep 1

echo "start rabbitmq ..."
docker start fae5f4f2ad5c
echo "rabbitmq started ..."

sleep 1

echo "start redis ..."
docker start cbaafb90ac7f
echo "redis started ..."

sleep 1

echo "start center ..."
docker start 62f3423882e9
echo "center started ..."

sleep 1

echo "start meta ..."
docker start bc9bdcfacaeb
echo "meta started ..."

sleep 1

echo "start dict ..."
docker start 8be8cdd202b3
echo "dict started ..."

sleep 1

echo "start audit ..."
docker start 352734f76347
echo "audit started ..."

sleep 1

echo "start view"
docker start 7cf7a6120742
echo "view stared ..."

sleep 1

echo "start api ..."
docker start 0b1d89bcfef9
echo "api started ..."

sleep 1

echo "start airflow-web ..."
docker start 0cf30ad49f01
echo "airflow-web started ..."

sleep 1

echo "start airflow-schedule ..."
docker start 6b61e4961efe
echo "airflow-schedule started ..."

sleep 1

echo "start airflow-worker ..."
docker start 08fca2285dbc
echo "airflow-worker started ..."

sleep 1

echo "all server started ..."