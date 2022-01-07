from MPC_Controller.common.Quadruped import Quadruped
from MPC_Controller.common.LegController import LegController
from FSM_States.ControlFSM import ControlFSM
from Parameters import Parameters
from StateEstimatorContainer import StateEstimatorContainer
from DesiredStateCommand import DesiredStateCommand

class MIT_Controller:
    def __init__(self, ) -> None:
        pass

    def initializeController(self,
                             _quadruped:Quadruped,
                             _stateEstimator:StateEstimatorContainer,
                             _legController:LegController,
                             _desiredStateCommand:DesiredStateCommand,
                             userParameters:Parameters):
        """Initializes the Control FSM"""
        self.userParameters = userParameters
        # self._gaitScheduler = GaitScheduler()

        self._controlFSM = ControlFSM(_quadruped, 
                                      _stateEstimator, 
                                      _legController,
                                      _desiredStateCommand,
                                      userParameters)

    def runController(self):
        """
        Calculate the commands for the leg controllers using the ControlFSM logic
        """
        # _gaitScheduler.step()

        # _desiredStateCommand.convertToStateCommands()

        # Run the Control FSM code
        self._controlFSM.runFSM()

    def getUserControlParameters(self):
        return self.userParameters
