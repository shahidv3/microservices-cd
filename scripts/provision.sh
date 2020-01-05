
echo "RUNNING ansible-playbook -c local --inventory-file=hosts --extra-vars='ansible_ssh_user=vagrant' --user=vagrant " $@
ansible-playbook -c local --inventory-file=hosts --extra-vars='ansible_ssh_user=vagrant' --user=vagrant "$@"
