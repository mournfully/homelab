# ansible

Ansible playbooks describe the desired state of your infrastructure for ansible to provision.
- `pve` playbooks target the proxmox hypervisor host.
- `dev` playbooks target a virtual machine I use to host a few legacy docker containers.
- `k8s` playbooks target my personal kubernetes cluster.

A few commands to keep in mind are as follows.
- If you're targetting `pve` use `ssh pve` first and authenticate via 2fa, so that ansible can reuse that connection via ssh multiplexing.
- `ansible servers -m ping`
- `ansible servers -m shell -a 'hostname'`

Run `./scripts/update-ansible-main.sh` to automatically append the latest playbooks under `ansible/playbooks/*` to `ansible/main.yml`.
