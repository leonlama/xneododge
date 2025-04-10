class BaseArtifact:
    def __init__(self, artifact_type, cooldown_duration):
        self.artifact_type = artifact_type
        self.cooldown_duration = cooldown_duration

    def activate(self, player):
        raise NotImplementedError
