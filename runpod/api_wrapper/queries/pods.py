def generate_pod_query(pod_id):
    '''
    Generate a query for a specific pod
    '''

    return f"""
    query Pod {{
        pod(input: {{podId: "{pod_id}"}}) {{
            id
            name
            runtime {{
                uptimeInSeconds
                ports {{
                    ip
                    isIpPublic
                    privatePort
                    publicPort
                    type
                }}
                gpus {{
                    id
                    gpuUtilPercent
                    memoryUtilPercent
                }}
                container {{
                    cpuPercent
                    memoryPercent
                }}
            }}
        }}
    }}
    """