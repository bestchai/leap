#!/bin/bash -x
# for i in {1..11}
# do
#     ./create-vm.sh t p${i} proj1full t1 getreadytoBl0ckDra@wP
# done

./create-sites.sh
./create-client.sh
./create-cloud.sh

# wait for all the above to complete

for job in `jobs -p`
do
echo $job
wait $job
done
