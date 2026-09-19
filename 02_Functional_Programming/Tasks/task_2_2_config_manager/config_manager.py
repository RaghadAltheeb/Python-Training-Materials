system_env="Development"
def deploy_to_production():
    global system_env
    system_env="Production"
    
    def log_deployment():
        print(f"Deploying from Development to Production.")
    return log_deployment()

print(system_env)
deploy_to_production()
print(system_env)

