# ansible

Ansible playbooks describe the desired state of your infrastructure for ansible to provision.
- `pve` playbooks target the proxmox hypervisor host.
- `dev` playbooks target a virtual machine I use to host a few legacy docker containers.
- `k8s` playbooks target my personal kubernetes cluster.

A few commands to keep in mind are as follows.
- If you're targetting `pve` use `ssh pve` first and authenticate via 2fa, so that ansible can reuse that connection via ssh multiplexing.
- `ansible homeprod -m ping`
- `ansible homeprod -m shell -a 'hostname'`
- `ansible-playbook main.yml`

Setup a [pre-commit hook](../scripts/add-vault-hook.sh) to ensure that ansible-vault (`ansible/inventory/group_vars/homeprod.yml`) can't ever be commited unless it's encrypted. [^1]

Run `./scripts/update-ansible-main.sh` to automatically append the latest playbooks under `ansible/playbooks/*` to `ansible/main.yml`.

[^1]: [compose-secret-mgt/git-init.sh at 8341948a3c2d2efc9677c4c2faf5d3d6d3becdf8 · ironicbadger/compose-secret-mgt](https://github.com/ironicbadger/compose-secret-mgt/blob/8341948a3c2d2efc9677c4c2faf5d3d6d3becdf8/git-init.sh)
