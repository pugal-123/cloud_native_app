from kubernetes import config

try:
    config.load_kube_config()
    current_context = config.list_kube_config_contexts()[1]
    print("Current context:", current_context)
except Exception as e:
    print("Error:", e)
