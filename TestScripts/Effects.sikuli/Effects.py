import utils
reload(utils)
from utils import *
import os
import sys
from sikuli import *

import unittest
        
class TestEffects(unittest.TestCase):

    def setUp(self):       
        utils.cleanCache_And_LaunchPRE()
                  
    def test_UI_Effects(self):
        utils.clickElement(utils.getBaselineImg('Button_GoalScreen_CloseGoalScreen.png'))
        utils.findElement(utils.getBaselineImg('BaselineIMG_PREMenuBar.png'))

        utils.clickElement(utils.getBaselineImg('Button_ExpertRoom.png'))         
        utils.findElement(utils.getBaselineImg('BaselineIMG_ExportRoomTimeline.png'))
        wait(2)
        utils.findElement(utils.getBaselineImg('Button_RHSPanels_Effects.png'))
        
        utils.clickElement(utils.getBaselineImg('Button_RHSPanels_Effects.png'))
        utils.findElement(utils.getBaselineImg('DropDown_EffectsPanel_AllCategories.png'))
        utils.clickElement(utils.getBaselineImg('DropDown_EffectsPanel_AllCategories.png'))
        utils.findElement(utils.getBaselineImg('BaselineIMG_Effects_AllCategories.png'))

        utils.clickElement(utils.getBaselineImg('Effects_Category_AdvancedAdjustments.png'))
        utils.assertElementExists(utils.getBaselineImg('Effects_Category_AdvancedAdjustments_items.png'))
        utils.clickElement(utils.getBaselineImg('Button_EffectCategories_Next.png'))
       
        utils.assertElementExists(utils.getBaselineImg('Effects_Category_BlurSharpen_items.png'))   
        utils.clickElement(utils.getBaselineImg('Button_EffectCategories_Next.png'))
        
        utils.assertElementExists(utils.getBaselineImg('Effects_Category_Channel_items.png'))
        utils.clickElement(utils.getBaselineImg('Button_EffectCategories_Next.png'))

        utils.assertElementExists(utils.getBaselineImg('Effects_Categories_ColorCorrection_items.png'))
        utils.clickElement(utils.getBaselineImg('Button_EffectCategories_Next.png'))

        utils.assertElementExists(utils.getBaselineImg('Effects_Categories_Distort_items.png'))
        utils.clickElement(utils.getBaselineImg('Button_EffectCategories_Next.png'))

        utils.assertElementExists(utils.getBaselineImg('Effects_Categories_Generate_items.png'))
        utils.clickElement(utils.getBaselineImg('Button_EffectCategories_Next.png'))

        utils.assertElementExists(utils.getBaselineImg('Effects_Categories_ImageControl_items.png'))
        utils.clickElement(utils.getBaselineImg('Button_EffectCategories_Next.png'))

        utils.assertElementExists(utils.getBaselineImg('Effects_Categories_Keying_items.png'))
        utils.clickElement(utils.getBaselineImg('Button_EffectCategories_Next.png'))

        utils.assertElementExists(utils.getBaselineImg('Effects_Categories_NewBlueArtEffects_items.png'))
        utils.clickElement(utils.getBaselineImg('Button_EffectCategories_Next.png'))

        utils.assertElementExists(utils.getBaselineImg('Effects_Categories_NewBlueCartoonrPlus_items.png'))
        utils.clickElement(utils.getBaselineImg('Button_EffectCategories_Next.png'))

        utils.assertElementExists(utils.getBaselineImg('Effects_Categories_NewBlueFilmLooks_items.png'))
        utils.clickElement(utils.getBaselineImg('Button_EffectCategories_Next.png'))

        utils.assertElementExists(utils.getBaselineImg('Effects_Categories_Perspective_items.png'))
        utils.clickElement(utils.getBaselineImg('Button_EffectCategories_Next.png'))

        utils.assertElementExists(utils.getBaselineImg('Effects_Categories_Pixelate_items.png'))
        utils.clickElement(utils.getBaselineImg('Button_EffectCategories_Next.png'))

        utils.assertElementExists(utils.getBaselineImg('Effects_Categories_Render_items.png'))
        utils.clickElement(utils.getBaselineImg('Button_EffectCategories_Next.png'))

        utils.assertElementExists(utils.getBaselineImg('Effects_Categories_Stylize_items.png'))
        utils.clickElement(utils.getBaselineImg('Button_EffectCategories_Next.png'))

        utils.assertElementExists(utils.getBaselineImg('Effects_Categories_Time_items.png'))
        utils.clickElement(utils.getBaselineImg('Button_EffectCategories_Next.png'))

        utils.assertElementExists(utils.getBaselineImg('Effects_Categories_Transform_items.png'))
        utils.clickElement(utils.getBaselineImg('Button_EffectCategories_Next.png'))

        utils.assertElementExists(utils.getBaselineImg('Effects_Categories_VideoMerge_items.png'))
        utils.clickElement(utils.getBaselineImg('Button_EffectCategories_Next.png'))
        
        wait(2)
        utils.clickElement(utils.getBaselineImg('Button_EffectCategories_Next.png'))

        utils.assertElementExists(utils.getBaselineImg('Effects_Categories_HollywoodLooks_items.png'))              
    
    def tearDown(self):
       utils.closePRE()         

