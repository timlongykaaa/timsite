curl -s https://www.binance.com/fr/price/ethereum  > /home/ec2-user/projetlinux/data.txt 
ethereum=$(cat /home/ec2-user/projetlinux/data.txt | grep -oP '(?<="price":")[^"]*')
date_monsite=$(date +"%Y-%m-%d %T")
echo $ethereum";"$date_monsite >> /home/ec2-user/projetlinux/data1.csv
 

