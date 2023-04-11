rm ../.git/hooks/pre-commit
touch ../.git/hooks/pre-commit
chmod +x ../.git/hooks/pre-commit
cat <<EOT >> ../.git/hooks/pre-commit
if ( cat ansible/inventory/group_vars/homeprod.yml | grep -q "\$ANSIBLE_VAULT;" ); then
    echo "\e[38;5;108mVault Encrypted. Safe to commit.\e[0m"
else
    echo "\e[38;5;208mVault not encrypted! Run 'ansible-vault encrypt homeprod.yml' and try again.\e[0m"
    exit 1
fi
EOT
